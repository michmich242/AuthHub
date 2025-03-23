import requests
import time
from colorama import init, Fore
from requests.structures import CaseInsensitiveDict
import requests
from hashlib import pbkdf2_hmac
import os
from github import Github
from github import Auth




def createhash(the_input):
    #hash = hashlib.sha256()
    #hash.update(the_input.encode())
    #return hash.hexdigest()

    hash = pbkdf2_hmac("sha256",the_input.encode(), "generate sogwgtawg".encode(), 1000000)
    return hash.hex()
#--------------------------------------------------------------------------------------------------------------------------------


init()
question = int(input(("Program\n    1. Login\n    2. Reset Username\n    3. Reset Password\n    Enter Choice: ")))
def logging(question):
    while question != 1 or question != 2 or question != 3:
        authtoken = Auth.Token("YOUR-OWN-KEY")
        g = Github(auth=authtoken)

        
        if question == 3:
            username = input("Enter your username: ")
            url = f"https://raw.githubusercontent.com/YOUR-GITHUB-USER/YOUR-GITHUB-REPO/main/Users/{username}/{username}.arz"
            headers = CaseInsensitiveDict()
            headers["Authorization"] = "token " + "YOUR-OWN-KEY"
            r = requests.get(url, headers=headers, stream=True) 
            first = str(r.content).replace("b'", "")
            second = first.replace("\\r", "")
            third = second.replace("\\n'", "")
            hashed_website_username = third.replace("'", "")



            
            while createhash(username) != hashed_website_username:
                username = input("You have entered a wrong username, try again: ")
                hash_oldname = createhash(username)
                url = f"https://raw.githubusercontent.com/YOUR-GITHUB-USER/YOUR-GITHUB-REPO/main/Users/{username}/{username}.arz"
                headers = CaseInsensitiveDict()
                headers["Authorization"] = "token " + "YOUR-OWN-KEY"
                r = requests.get(url, headers=headers, stream=True) 
                first = str(r.content).replace("b'", "")
                second = first.replace("\\r", "")
                third = second.replace("\\n'", "")
                hashed_website_username = third.replace("'", "")




            old_password = input("Enter your old password: ")
            old_password_hash = createhash(old_password)
            url = f"https://raw.githubusercontent.com/YOUR-GITHUB-USER/YOUR-GITHUB-REPO/main/Users/{username}/pass_{username}.arz"
            headers = CaseInsensitiveDict()
            headers["Authorization"] = "token " + "YOUR-OWN-KEY"
            r = requests.get(url, headers=headers, stream=True)
            first = str(r.content).replace("b'", "")
            second = first.replace("\\r", "")
            third = second.replace("\\n'", "")
            fourth = third.replace("'", "")
            fifth  = fourth.replace("\n", "")
            hashed_website_password = fifth.replace("'", "")





            while old_password_hash != hashed_website_password:
                retry_password = input("You have entered the wrong password, try again: ")
                old_password_hash = createhash(retry_password)
                
            new_password = input("Enter your new password: ")
            new_password_hash = createhash(new_password)
            
            repo = g.get_repo("YOUR-GITHUB-USER/YOUR-GITHUB-REPO")
            repo_checking_pass = repo.get_contents(f"Users/{username}", ref="main")
            for repo_in_loop in repo_checking_pass:
                if repo_in_loop.path == f"Users/{username}/pass_{username}.arz":
                    repo.update_file(repo_in_loop.path, "user has updated password", new_password_hash, repo_in_loop.sha, branch="main")
                    input("Successfully changed password. Please wait at least 5 - 7 minutes to process, then Restart the application to login.")
                    exit()
                    
            




        elif question == 2:
            old_name = input("Enter your old username: ")
            url = f"https://raw.githubusercontent.com/YOUR-GITHUB-USER/YOUR-GITHUB-REPO/main/Users/{old_name}/{old_name}.arz"
            headers = CaseInsensitiveDict()
            headers["Authorization"] = "token " + "YOUR-OWN-KEY"
            r = requests.get(url, headers=headers, stream=True) 
            first = str(r.content).replace("b'", "")
            second = first.replace("\\r", "")
            third = second.replace("\\n'", "")
            hashed_website_username = second.replace("'", "")
            hash_oldname = createhash(old_name)


            if hash_oldname == hashed_website_username:
                retry_oldname = old_name

            
            while hash_oldname != hashed_website_username:

                retry_oldname = input("You have entered a wrong username, try again: ")
                hash_oldname = createhash(retry_oldname)
                url = f"https://raw.githubusercontent.com/YOUR-GITHUB-USER/YOUR-GITHUB-REPO/main/Users/{retry_oldname}/{retry_oldname}.arz"
                headers = CaseInsensitiveDict()
                headers["Authorization"] = "token " + "YOUR-OWN-KEY"
                r = requests.get(url, headers=headers, stream=True) 
                first = str(r.content).replace("b'", "")
                second = first.replace("\\r", "")
                third = second.replace("\\n'", "")
                hashed_website_username = third.replace("'", "")


            your_pass_word = input("Enter your password: ")

            



            url = f"https://raw.githubusercontent.com/YOUR-GITHUB-USER/YOUR-GITHUB-REPO/main/Users/{retry_oldname}/pass_{retry_oldname}.arz"
            headers = CaseInsensitiveDict()
            headers["Authorization"] = "token " + "YOUR-OWN-KEY"
            r = requests.get(url, headers=headers, stream=True) 
            first = str(r.content).replace("b'", "")
            second = first.replace("\\r", "")
            third = second.replace("\\n'", "")
            hashed_website_password = third.replace("'", "")


            while createhash(your_pass_word) != hashed_website_password:
                your_pass_word = input("Wrong password, try again: ")

            new_name = input("Enter your new username: ")
            hashed_name = createhash(new_name)

            authtoken = Auth.Token("YOUR-OWN-KEY")
            g = Github(auth=authtoken)  
            repo = g.get_repo("YOUR-GITHUB-USER/YOUR-GITHUB-REPO")

            repo.create_file(f"Users/{new_name}/{new_name}.arz", "A user updated their username", f"{hashed_name}", branch="main")
            repo.create_file(f"Users/{new_name}/pass_{new_name}.arz", "A user updated their username", f"{hashed_website_password}", branch="main")

            contents = repo.get_contents(f"Users/{retry_oldname}", ref="main")
            for content in contents:
                print(content)
                repo.delete_file(content.path, f"Changed username deleting old files", content.sha, branch="main")
            input("Successfully Changed username. Restart the Application for the new login.")
            exit()        



        elif question == 1:
            #-----------------------------Logging in Github-------------------------
            catch = input("Enter your username: ")
            catch2 = input("Enter your password: ")
            username = createhash(catch)
            password = createhash(catch2)


            url = f"https://raw.githubusercontent.com/YOUR-GITHUB-USER/YOUR-GITHUB-REPO/main/Users/{catch}/{catch}.arz"
            headers = CaseInsensitiveDict()
            headers["Authorization"] = "token " + "YOUR-OWN-KEY"
            r = requests.get(url, headers=headers, stream=True) 
            first = str(r.content).replace("b'", "")
            second = first.replace("\\r", "")
            third = second.replace("\\n'", "")
            hashed_website_username =  third.replace("'", "")

            url = f"https://raw.githubusercontent.com/YOUR-GITHUB-USER/YOUR-GITHUB-REPO/main/Users/{catch}/pass_{catch}.arz"
            headers = CaseInsensitiveDict()
            headers["Authorization"] = "token " + "YOUR-OWN-KEY"
            r = requests.get(url, headers=headers, stream=True) 
            first = str(r.content).replace("b'", "")
            second = first.replace("\\r", "")
            third = second.replace("\\n'", "")
            hashed_website_password =  third.replace("'", "")






            if(username.strip() == hashed_website_username.strip() and hashed_website_password.strip() == password.strip()):
                print(f"{Fore.GREEN}Login Successful")
                return True
                
            else:
                print(f"{Fore.RED}Login Failed")
                return False
        
            
        else:
            print("That is not a valid option try again")
            question = int(input(("Program\n    1. Login\n    2. Reset Username\n    3. Reset Password\n    Enter Choice: ")))
            