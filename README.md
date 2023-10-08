# McStatsX Discord Bot

![McStatsX Banner](https://example.com/banner.png) <!-- Add a banner image or logo for your project -->

McStatsX is a versatile Discord bot designed to provide real-time Minecraft server status updates to your Discord community. Whether you run a gaming server or want to keep your friends informed, McStatsX has you covered.

## Features

- **Server Status**: Keep your community updated with real-time Minecraft server status, including player count, maximum player capacity, and online/offline status.

- **Emoji Customization**: Easily configure emojis for online and offline server statuses to match your server's style.

- **User-Friendly**: McStatsX is designed with simplicity in mind, making it easy to set up and use.

- **Embed Messages**: Server status updates are delivered in beautifully formatted embed messages for clarity and aesthetics.

- **Automatic Updates**: McStatsX posts the initial server status message if not present in the specified channel and continuously updates it every 30 seconds.

- **Open Source**: McStatsX is an open-source project, allowing you to customize and adapt it to your specific needs.

## Setup

1. Clone this repository to your local machine.
2. Create a `config.py` file based on the provided `config_sample.py` template.
3. Install the required packages using `pip install -r requirements.txt`.
4. Run the bot using `python main.py`.

## Configuration

- `TOKEN`: Your Discord bot token.
- `SERVER_IP`: The Minecraft server IP address.
- `SERVER_PORT`: The Minecraft server port.
- `CHANNEL_ID`: The Discord channel ID where server status updates will be posted.
- `ONLINE_EMOJI`: Emoji for online status.
- `OFFLINE_EMOJI`: Emoji for offline status.

## Usage

- Invite the bot to your Discord server.
- Make sure the bot has necessary permissions to read and send messages in the specified channel.
- The bot will automatically post server status updates every 30 seconds.

## Contribution

Contributions are welcome! If you have any ideas for improvements or bug fixes, feel free to create a pull request or open an issue.

## License

This project is licensed under the [MIT License](LICENSE).

---

**Disclaimer**: McStatsX is an independent project and is not affiliated with or endorsed by Mojang or Microsoft.
