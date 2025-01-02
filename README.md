# AO3 Bulk Downloader and Scheduler

A tool to download multiple works from Archive of Our Own (AO3) and schedule future posts/updates.

## Features

- Bulk download works from AO3 using one or multiple links
- Save works in multiple formats (HTML, EPUB, PDF)
- Schedule future posts and chapter updates
- Manage multiple works and their posting schedules through a simple interface

## Installation

1. Ensure you have Python 3.8 or higher installed
2. Clone this repository:
```bash
git clone https://github.com/yourusername/ao3-downloader-scheduler
cd ao3-downloader-scheduler
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Downloading Works

To download works, you can either:

1. Use the command line:
```bash
python ao3_downloader.py --url "https://archiveofourown.org/works/..."
```

2. Use multiple URLs:
```bash
python ao3_downloader.py --urls urls.txt
```
Where `urls.txt` contains one AO3 URL per line.

### Scheduling Posts

1. Launch the scheduler interface:
```bash
python ao3_scheduler.py
```

2. In the scheduler interface:
   - Select the work you want to schedule
   - Choose the posting date and time
   - Set up recurring schedules for multi-chapter works
   - Preview scheduled posts

## Configuration

Create a `config.json` file in the root directory:
```json
{
    "download_format": "EPUB",
    "download_path": "./downloads",
    "credentials": {
        "username": "your_ao3_username"
    }
}
```

## Authentication

To use the posting scheduler, you'll need to log in to your AO3 account:

1. Run the authentication setup:
```bash
python auth_setup.py
```

2. Follow the prompts to enter your credentials
3. Your session will be saved securely for future use

## Privacy and Security

- Your AO3 credentials are stored securely using environment variables
- Downloaded works are saved locally only
- The tool respects AO3's Terms of Service and rate limits

## Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) before submitting pull requests.

## Limitations

- Works marked as "Registered Users Only" require authentication
- Scheduled posts require a stable internet connection at the time of posting
- Rate limiting applies to protect AO3's servers

## Troubleshooting

Common issues and solutions:

1. **Download fails**
   - Check your internet connection
   - Verify the URL is accessible
   - Ensure you're logged in for restricted works

2. **Scheduler issues**
   - Confirm your system time is correct
   - Check your AO3 session hasn't expired
   - Verify you have proper permissions for the work

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built using the AO3 API guidelines
- Inspired by the AO3 community's needs
- Thanks to all contributors and users

## Support

- Create an issue on GitHub for bug reports
- Join our Discord community for help