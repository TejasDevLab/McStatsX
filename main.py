import discord
import asyncio
from mcstatus import MinecraftServer
import config  # Import the configuration from config.py

# Initialize Discord client
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
client = discord.Client(intents=intents)

# Function to get Minecraft server status and post the initial message if needed
async def get_server_status():
    await client.wait_until_ready()  # Wait for the bot to be ready
    while not client.is_closed():
        try:
            server = MinecraftServer(config.SERVER_IP, config.SERVER_PORT)
            status = server.status()

            # Determine the server status emoji
            status_emoji = config.ONLINE_EMOJI if status.players.online > 0 else config.OFFLINE_EMOJI

            # Create an embed with server status information
            embed = discord.Embed(title="Minecraft Server Status", color=0x00ff00)
            embed.add_field(name="Server IP", value=config.SERVER_IP, inline=True)
            embed.add_field(name="Server Port", value=config.SERVER_PORT, inline=True)
            embed.add_field(name="Status", value=f"{status_emoji} {status.description}", inline=True)
            embed.add_field(name="Online Players", value=status.players.online, inline=True)
            embed.add_field(name="Max Players", value=status.players.max, inline=True)

            # Get the specified channel
            channel = client.get_channel(config.CHANNEL_ID)

            # Check if a message has been posted in the channel, if not, post the initial message
            async for message in channel.history(limit=1):
                await message.edit(embed=embed)
                break
            else:
                await channel.send(embed=embed)

        except ConnectionRefusedError:
            error_message = "Server is currently offline or the IP and port are incorrect."
            await channel.send(error_message)
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            await channel.send(error_message)

        await asyncio.sleep(30)  # Check every 30 seconds

# Event when the bot is ready
@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

# Start the bot and continuously check the server status
client.loop.create_task(get_server_status())
client.run(config.TOKEN)
