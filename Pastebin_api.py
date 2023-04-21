import requests

API_POST_URL = 'https://pastebin.com/api/api_post.php'
DEVELOPER_API_KEY = '3VDIZtEsuBF0hrQTShCSGqyAF6LM-m8D'

def main():
    past_url = post_new_paste('whatever paste', 'this is me')
    pass

def post_new_paste(title, body_text, expiration_period ='10M', publicly_listed =True):
    """Creates a new public PasteBin paste 

    Args:
        title(str): Paste title
        body_text (str): Paste body text
        expriation_period (str, optional): How long the paste will last.(see https://pastebin.com/doc_api) Defaults to '10M'.
        publicly_listed (bool, optional): Whether the paste is listed or not. Defaults to True.

    Retuens:
       str: URL of the new paste. None if unsuccessful.
        """

    # Create dictionary of parameter values
    params = {
        'api_dev_key': DEVELOPER_API_KEY,
        'api_option': 'paste',
        'api_paste_code': body_text
        'api_paste_name': title,
        'api_paste_expire_date': expiration_period,
        'api_paste_private': 0 if publicly_listed else 1
    }
    

    # Sent the POST request to the PasteBin API
    print("Posting new paste to PasteBin....", end='')
    resp_msg = requests.post(API_POST_URL, data=params)

    # Check if paste was created successfully
    if resp_msg.status_code == requests.codes.ok:
        print('success')
        print(f'URL of new paste: {resp_msg.text}')
        return resp_msg.text
    else:
        print("failure")
        print(f"Response code: {resp_msg.status_code} ({resp_msg.reason})")
        print(f"Error: {resp_msg.text}")
    pass 

if __name__ == "__main__":
    main()

