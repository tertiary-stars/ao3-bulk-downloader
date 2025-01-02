# AO3 Bulk Downloader and Scheduler

A tool to download multiple works from Archive of Our Own (AO3) and schedule future posts/updates.

## Features

- Bulk download works from AO3 using one or multiple links
- Save works in multiple formats (HTML, EPUB, PDF, MOBI)
- Schedule future posts and chapter updates (upcoming)
- Manage multiple works and their posting schedules through a simple interface (upcoming)

## Installation

1. Ensure you have Python 3.8 or higher installed
2. Clone this repository:
```bash
git clone https://github.com/tertiary-stars/ao3-downloader-scheduler
cd ao3-downloader-scheduler
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Set up

Edit the `config.json` file in the root directory to include your AO3 username and password:
```json
{
    "download_format": "EPUB",
    "download_path": "./downloads",
    "credentials": {"AO3_USERNAME":"username", 
                    "AO3_PASSWORD":"password"
    }
}
```
Download format takes all formats AO3 allows, it is not case sensitive. 

## Authentication

To use the bulk downloader or scheduler, you'll need to log in to your AO3 account:

1. Ensure you edited config.json file with your credentials
2. Run the authentication setup:
```bash
python auth_setup.py
```
This is to ensure restricted works can be downloaded, too.

## Downloading Works

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

## Disclaimers
- Your AO3 credentials are stored securely using environment variables. We have absolutely **no** access to them.
- Downloaded works are saved locally only. 
- The tool respects AO3's Terms of Service and rate limits.

## Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) before submitting pull requests.

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
