
# TUS Collector

This is a simple tool that collects TUS from side addresses to main address. Especially for Crabada players who has multiple accounts. 

 1. [Install Python](#install-python)
 2. [Get Your Address](#get-your-address)
 3. [Get Your Private Key](#get-your-private-key)
 4. [Set Main Address](#set-main-address)
 5. [Run Program](#run-program)
 
 
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

<img width="405" alt="Screen Shot 2022-09-12 at 11 20 15" src="https://user-images.githubusercontent.com/60021484/189606234-95cf6cc5-5396-49f3-9d02-02f418f57f01.png">

- Click **Account Details**.

<img width="405" alt="Screen Shot 2022-09-12 at 11 10 18" src="https://user-images.githubusercontent.com/60021484/189605733-22c6cc8c-e902-41a7-8257-83869a43ac3e.png">

- Click **Export Private Key**.

<img width="405" alt="Screen Shot 2022-09-12 at 11 10 37" src="https://user-images.githubusercontent.com/60021484/189605778-61ca4955-ca3b-4f8c-b345-e3517bdfd28f.png">

- Write your **Metamask password** to the area and click **Confirm**. You will see your private key.

<img width="405" alt="Screen Shot 2022-09-12 at 11 11 11" src="https://user-images.githubusercontent.com/60021484/189605899-49e26118-7f7c-452d-8278-00231c141ada.png">

- Copy your **private key**.

<img width="405" alt="Screen Shot 2022-09-12 at 11 12 17" src="https://user-images.githubusercontent.com/60021484/189605924-46799f1c-9f9e-4c92-8fab-903b81351340.png">


### Set Main Address

- Open config.py under **src/utils** directory. You can use Visual Studio Code to edit the code, or Notepad will be useful.

<img width="334" alt="Screen Shot 2022-09-12 at 11 37 48" src="https://user-images.githubusercontent.com/60021484/189614835-f9043725-e6a4-4a09-8145-a9b069d4fe18.png">

- Put your main address as shown below. (This is the **destination address** for TUS to be sent).

<img width="1357" alt="main address" src="https://user-images.githubusercontent.com/60021484/189614987-7476ebb9-bdcd-4ebc-9b39-1073bfbf4595.png">

### Set Side Addresses and Private Keys
- Open config.py under **src/utils** directory. You can use Visual Studio Code to edit the code, or Notepad will be useful.

- Put your addresses to the left side. Private keys should be put to the right side like below.

  - Address 
  
  <img width="1357" alt="address" src="https://user-images.githubusercontent.com/60021484/189615214-df152b16-9ab2-45a5-90a3-0a4a3cc454ae.png">
  
  - Private key
  
  <img width="1357" alt="private key" src="https://user-images.githubusercontent.com/60021484/189615276-9f405fa7-7e2f-49aa-9b06-7e1c993d97e1.png">

### Run program

- Open terminal in program's directory.

- For Mac

  ```python3 main.py```

- For Windows

  ```python main.py```
  
<img width="953" alt="Screen Shot 2022-09-12 at 12 20 29" src="https://user-images.githubusercontent.com/60021484/189618397-cc2e4d65-c056-43ab-9eef-056792569e15.png">
