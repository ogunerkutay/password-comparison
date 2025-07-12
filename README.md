# Password Comparison Tool

A Python utility for comparing password CSV files exported from different browsers or password managers to identify conflicts and differences.

## Features

- **Conflict Detection**: Finds entries with the same URL and username but different passwords
- **Unique Entry Identification**: Lists entries that exist in only one file
- **Case-Insensitive Comparison**: Normalizes URLs and usernames for robust comparison
- **Error Handling**: Provides clear error messages for common issues

## Requirements

- Python 3.x
- No additional dependencies required (uses standard library only)

## Usage

### Command Line

```bash
python compare.py <file1> <file2>
```

### Examples

Compare Chrome and Edge password exports:
```bash
python compare.py "Chrome Passwords.csv" "Microsoft Edge Passwords.csv"
```

Compare any two password CSV files:
```bash
python compare.py passwords_backup.csv current_passwords.csv
```

### Expected CSV Format

The CSV files should contain the following columns:
- `url` - The website URL
- `username` - The username/email used for login
- `password` - The password for the account

Example CSV structure:
```csv
url,username,password
https://example.com,user@email.com,mypassword123
https://github.com,username,securepass456
```

## Output Types

### 1. Conflicts
Shows entries where the same URL and username combination has different passwords in the two files:
```
--- Conflicts (same url and username, different password) ---
URL: https://example.com, Username: user@email.com
  Password in file1.csv: oldpassword
  Password in file2.csv: newpassword
```

### 2. Unique Entries
Lists entries that exist in only one file:
```
--- Unique entries in file1.csv ---
URL: https://uniquesite.com, Username: user@email.com, Password: password123

--- Unique entries in file2.csv ---
URL: https://anothersite.com, Username: different@email.com, Password: pass456
```

### 3. No Differences
If files are identical:
```
No conflicts or differences found between the two files.
```

## How to Export Password Files

### Chrome
1. Open Chrome Settings
2. Go to Autofill → Password Manager
3. Click the three dots menu → Export passwords
4. Save as CSV file

### Microsoft Edge
1. Open Edge Settings
2. Go to Profiles → Passwords
3. Click the three dots menu → Export passwords
4. Save as CSV file

### Other Browsers/Password Managers
Most modern browsers and password managers support CSV export. Look for "Export" options in their password management sections.

## Technical Details

- **Normalization**: URLs and usernames are converted to lowercase and stripped of whitespace for comparison
- **Duplicate Handling**: If the same normalized key appears multiple times in a file, the last entry takes precedence
- **Memory Efficient**: Loads entire files into memory for fast comparison (suitable for typical password file sizes)

## Error Handling

The tool handles common errors gracefully:
- File not found
- Invalid CSV format
- Missing required columns
- Encoding issues

## Security Notes

- This tool only reads CSV files locally - no data is transmitted
- Be careful with password files - delete exports after use
- Consider using encrypted storage for password backups
- The tool displays passwords in plaintext output - use in secure environments only

## Contributing

Feel free to submit issues or pull requests to improve this tool.

## License

This project is open source. Use at your own risk and ensure you handle password data securely.
