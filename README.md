
# TUS Collector

This is a simple tool that collects TUS from side addresses to main address. Especially for Crabada players who has multiple accounts. 

## Set Up
 1. [Install Python](#install-python)
 2. [Get Your Address](#get-your-address)
 3. [Get Your Private Key](#get-your-private-key)
 4. [Set Main Address](#set-main-address)
 5. [Set Side Addresses and Private Keys](#set-side-addresses-and-private-keys)
 6. [Run Program](#run-program)
 
 **Options** are under **config.py**, you can change your preferences (Floor transfer limit, leave amount etc.) through this file
### Install Python

Firstly, Python3 should be installed on your computer. You can download Python from the link below.

- https://www.python.org/downloads/

Then **web3.py** package should be installed. 

- Open **Terminal** or **Cmd**:

- For Mac:
`pip3 install web3`

- For Windows:
`pip install web3`
 
### Get Your Address
- Open **Metamask** extension

- Click to the shown area. Your address will be copied to clipboard.

<img width="405" alt="Screen Shot 2022-09-12 at 11 21 46" src="https://user-images.githubusercontent.com/60021484/189613923-2d75d3a9-79d1-4d0e-a3ee-aeee7d0dfaaa.png">

### Get Your Private Key
- Open **Metamask** extension.

- Click **three dots** on the top right.

- Click **Account Details**.

- Click **Export Private Key**.

- Write your **Metamask password** to the area and click **Confirm**. You will see your private key.

- Copy your **private key**.

- Wait for GIF below.

![howToGetPrivateKey](https://user-images.githubusercontent.com/60021484/189709264-af5cb80f-b286-4d10-9720-f3bd27db6f59.gif)

### Set Main Address

- Open config.py under **src/utils** directory. You can use Visual Studio Code to edit the code, or Notepad will be useful.

<img width="334" alt="Screen Shot 2022-09-12 at 11 37 48" src="https://user-images.githubusercontent.com/60021484/189614835-f9043725-e6a4-4a09-8145-a9b069d4fe18.png">

- Put your main address as shown below. (This is the **destination address** for TUS to be sent).

<img width="1357" alt="main address" src="https://user-images.githubusercontent.com/60021484/189614987-7476ebb9-bdcd-4ebc-9b39-1073bfbf4595.png">

### Set Side Addresses and Private Keys
- Open **config.py** under **src/utils** directory. You can use Visual Studio Code to edit the code, or Notepad will be useful.

- Put your addresses to the left side. Private keys should be at the right side like below.

- ! **Warning:** Don't put your main address inside this dictionary.

![Screen Shot 2022-09-12 at 20 00 07](https://user-images.githubusercontent.com/60021484/189713463-33500679-5726-4997-ac94-fa1f3c30eaf5.png)

### Run program

- Open terminal in program's directory.

- For Mac

  ```python3 main.py```

- For Windows

  ```python main.py```
  
<img width="953" alt="Screen Shot 2022-09-12 at 12 20 29" src="https://user-images.githubusercontent.com/60021484/189618397-cc2e4d65-c056-43ab-9eef-056792569e15.png">
