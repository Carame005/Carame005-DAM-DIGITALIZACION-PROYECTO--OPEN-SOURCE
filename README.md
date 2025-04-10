Aquí tienes el **README** traducido al inglés:

---

# **Project Description: Discord Bot in Python**  

Welcome to my first open-source project! This is a Python script designed to program a Discord bot.  

It’s a simple bot that handles basic slash commands, with the unique feature of being able to save images to a local folder on the device that runs the script.

## Motivation  

The main reason for developing this project was the need for a customized bot for my servers and my friends' servers. I wanted something with various features that we could test and expand over time.  

Additionally, this project is meant to help novice programmers interested in Discord bot development. With this base code, they can download it, try it out, and modify it as they like. I'm also open to suggestions and improvements to continue evolving the bot over time.  

## Usage Instructions  
### Prerequisites
1. Make sure you have `git` installed.
2. Have Python 3.8 or higher installed.
3. `pip` Python package manager.

### Clone the repository
```bash
git clone https://github.com/Carame005/Carame005-DAM-DIGITALIZACION-PROYECTO--OPEN-SOURCE.git
```

### Code
Detailed instructions are within the code itself, but here’s a summary:  

1. Open the `config.py` file and paste your **bot token** as a string (`"your_token_here"`).  
2. In the same file, you can customize settings such as the folder where files will be saved.  
3. Run the script from the `main.py` file to activate the bot.  
4. **Note:** If the commands don’t respond immediately, it may be due to a slight delay in synchronization with Discord. Just wait a few minutes and they should appear.  

## Example Videos
![Carameloh2](https://github.com/user-attachments/assets/3db09fe5-dfd1-43e2-976f-5b3e046c6e38)

This is Carameloh, my test bot, which will show us how to use this script on Discord.

### Insert the token and start the bot
![Usage example](https://github.com/user-attachments/assets/09af6fc5-bee6-49d7-9072-993a6538aead)

### Use the bot’s slash commands
![Example](https://github.com/user-attachments/assets/9de739ff-cea1-4f77-9f15-de55bd3dd645)

## Feature Example  
One of the bot's basic commands is:  

- `!savememe`: If you attach an image when using this command, the bot will automatically save it to a specific folder.  
  - The storage location is defined in `config.py`.  
  - Images are organized by the server ID to avoid conflicts when using the bot on multiple servers.  

For more information on additional features, refer to the **Wiki** section of the repository.  
