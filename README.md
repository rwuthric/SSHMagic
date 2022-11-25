# SSHMagic
SSH magic function for ipython.

Allows to execute commands on a remote machine via ```ssh```. Requires a password-less access to the remote machine.

## Usage
Load the extension with
```
%load_ext sshmagic
```
To execute some commands on the remote host, for example ```remote.host.com``` as user ```alice``` use:
```
%ssh alice@remote.host.com
pwd
ls
```
Note: this requires that the user executing this command has a SSH key-based authentifcation for the account ```alice``` setup.

## Installation
Create a local clone of this repository and in the root directory of the cloned code run:
```
pip install .
```

## Uninstall
Use
```
pip uninstall sshmagic
```

## Configure SSH Key-Based Authentication

### Step 1 - Creating SSH Keys
First a SSH key pair needs to be generated. If you already have generated previously a key pair
do not repeat it as otherwise you will overwrite it.
Open a terminal using the JupyterLab launcher and execute the following command:
```
ssh-keygen
```
The utility will prompt you to select a location for the keys that will be generated. 
By default, the keys will be stored in the ```~/.ssh``` directory within your user’s home directory.
The private key will be called ```id_rsa``` and the associated public key will be called ```id_rsa.pub```.

If you had previously generated an SSH key pair, you will be asked if you want to overwrite it.
If you choose to overwrite the key on disk, you will not be able to authenticate using the previous key anymore.

Next, you will be prompted to enter a passphrase for the key. As we need a password less access to the remote machine
for the ssh magics, provide an empty passphrase by simply pressing the ```ENTER``` key.
```
Output
Your identification has been saved in /home/username/.ssh/id_rsa.
Your public key has been saved in /home/username/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:CAjsV9M/tt5skazroTc1ZRGCBz+kGtYUIPhRvvZJYBs username@hostname
The key's randomart image is:
+---[RSA 3072]----+
|o   ..oo.++o ..  |
| o o +o.o.+...   |
|. . + oE.o.o  .  |
| . . oo.B+  .o   |
|  .   .=S.+ +    |
|      . o..*     |
|        .+= o    |
|        .=.+     |
|       .oo+      |
+----[SHA256]-----+
```

As your key is not protected by a passphrase, it is important to have appropriate file permissions of the generated keys.
The default permissions (```id_rsa``` only user has read/write access 
and ```id_rsa.pub``` user has read/write access and group and world has read access) 
created by ```ssh-keygen``` are the ones to use and should not be changed.

You can verify the file permissions with
```
ls ~/.ssh -l
```
```
Output
-rw------- 1 username group 2602 Sep  9 19:53 id_rsa
-rw-r--r-- 1 username group  571 Sep  9 19:53 id_rsa.pub
```

### Step 2 - Copy the SSH Public Key to The Remote Machine
Open a terminal with your JupyterLab launcher and type
```
ssh-copy-id username@remote_host
```
by using the appropriate username account on your remote_host.

You may see a message like this:
```
Output
The authenticity of host '207.0.93.14 (207.0.93.14)' can't be established.
ECDSA key fingerprint is fd:fd:d4:f9:77:fe:73:84:e1:55:00:ad:d6:6d:22:fe.
Are you sure you want to continue connecting (yes/no)? yes
```
This means that your local computer does not recognize the remote host. 
This will happen the first time you connect to a new host. Type ```yes``` 
and press the ```ENTER``` key to continue.

Next, the utility will prompt you for the password of the remote host user’s account:
```
Output
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
username@207.0.93.14's password:
```
Type in the password (your typing will not be displayed for security purposes) and press the ```ENTER``` key.
The utility will connect to the account on the remote host and copy the contents of your ```~/.ssh/id_rsa.pub key```
into a file in the remote account’s home ```~/.ssh``` directory called ```authorized_keys```.

You will see output that looks like this:
```
Output
Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'username@207.0.93.14'"
and check to make sure that only the key(s) you wanted were added.
```
At this point, your ```id_rsa.pub``` key has been uploaded to the remote account.

You can try to log to your remote machine by typing this command in the terminal of your JupyterLab:
```
ssh username@remote_host
```
and you should get access to it without any password prompt.
