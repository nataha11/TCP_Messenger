# TCP_Messenger

**TCP_Messenger** is a simple TCP messenger. Server receives messages from several clients at the same time and sends this message to other clients.<br/>

Usage:<br/>
1. Open terminal.<br/>
2. Make sure you have python3 installed:<br/>
```
sudo apt install python3
```
3. Download the project:<br/>
```
mkdir messenger
cd messenger
git init
git clone https://github.com/nataha11/TCP_Messenger.git
cd TCP_Messenger
chmod +x server.py client.py
```
4. Execute:<br/>
```
python3 server.py
```
Open another terminal(s) by Ctrl+Shift+T and run<br/>
```
python3 client.py
```
Then write your ip address and press Enter.<br/>
Write 'hello' and start messaging with yourself.<br/>

Thanks for using TCP_Messenger!
