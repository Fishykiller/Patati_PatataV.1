# Patati_PatataV.1
Another python project


INFOS: 

atabase

Chrome stores a website’s username and password in an SQLite database named Login Data. The tables that we are interested in is logins and the fields we need to fetch are origin_url, username_value, password_value.

The following code will connect to the database and do that operation for us.

#path to user's login data

data_path = os.path.expanduser('~')+"\AppData\Local\Google\Chrome\User Data\Default"

login_db = os.path.join(data_path, 'Login Data')

#db connect and query

c = sqlite3.connect(login_db)

cursor = c.cursor()

select_statement = "SELECT origin_url, username_value, password_value FROM logins"

cursor.execute(select_statement)

Credentials


Now that we have access to our database, let’s fetch all the data into login_data and then store it in a dictionary credential. The URL would be the key and the username + password tuple would be its value. But before we do that, we need to decrypt the passwords.



Decrypting Chrome’s passwords

At this point, it is worth noting that this is exclusive to a Windows machine. So, Chrome uses Windows’s API CryptProtectData to encrypt all your passwords using a random generated key from your session. Which means, technically, the only way you can decrypt it is with the same user logon credentials on the same machine using CryptUnprotectData. So yeah, your Windows is the one that is encrypting your passwords here! You’ll need the pywin32 module installed to import win32crypt.

This following code fetches the data, decrypts and saves the URL and credentials in the credential dictionary.

login_data = cursor.fetchall()

#URL: credentials dictionary

credential = {}

#decrytping the password

    for url, user_name, pwd, in login_data:
    
        pwd = win32crypt.CryptUnprotectData(pwd, None, None, None, 0) #Tuple
        
        credential[url] = (user_name, pwd[1])


Writing your username and passwords to a text file

Now that you have your decrypted passwords, all that you have to do is iterate over it and write it to a text file. Or simple, you can modify the following code to print it directly to the prompt (Just get rid of the text file parts and swap the write statement with print).

The following code writes the data to a text file.

#writing to a text file (CAUTION: Don't leave this text file around!)
prompt = raw_input("[.] Are you sure you want to write all this sensitive data to a text file? \n[.] <y> or <n>\n[>] ")
if prompt == 'y':
    with open('pwd.txt', 'w') as f:
        for url, credentials in credential.iteritems():
            if credentials[1]:
                f.write("\n"+url+"\n"+credentials[0].encode('utf-8')+ " | "+credentials[1]+"\n")
            else:
                f.write("\n"+url+"\n"+"USERNAME NOT FOUND | PASSWORD NOT FOUND \n")
            print "[.] Successfully written to pwd.txt!"
else:
    quit()
    
    
    
Swoopy

Here is your complete code to proudly steal your own passwords from Chrome using Python.

import os
import sqlite3
import win32crypt
#path to user's login data
data_path = os.path.expanduser('~')+"\AppData\Local\Google\Chrome\User Data\Default"
login_db = os.path.join(data_path, 'Login Data')
#db connect and query
c = sqlite3.connect(login_db)
cursor = c.cursor()
select_statement = "SELECT origin_url, username_value, password_value FROM logins"
cursor.execute(select_statement)
login_data = cursor.fetchall()
#URL: credentials dictionary
credential = {}
#decrytping the password
for url, user_name, pwd, in login_data:
	pwd = win32crypt.CryptUnprotectData(pwd, None, None, None, 0) #This returns a tuple description and the password
	credential[url] = (user_name, pwd[1])
#writing to a text file (CAUTION: Don't leave this text file around!)
prompt = raw_input("[.] Are you sure you want to write all this sensitive data to a text file? \n[.]  or \n[>] ")
if prompt == 'y':
	with open('pwd.txt', 'w') as f:
		for url, credentials in credential.iteritems():
			if credentials[1]:
				f.write("\n"+url+"\n"+credentials[0].encode('utf-8')+ " | "+credentials[1]+"\n")
			else:
				f.write("\n"+url+"\n"+"USERNAME NOT FOUND | PASSWORD NOT FOUND \n")
	print "[.] Successfully written to pwd.txt!"
else:
	quit()
