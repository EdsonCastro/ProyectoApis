# Include the Dropbox SDK
import dropbox

# Get your app key and secret from the Dropbox developer website
def actulizarNotasDropbox():
    app_key = '887r2dpkbvj5l3e'
    app_secret = 'lqd33odxs1ada3t'

    flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)


    # Have the user sign in and authorize this token
    #authorize_url = flow.start()
    #print '1. Go to: ' + authorize_url
    #print '2. Click "Allow" (you might have to log in first)'
    #print '3. Copy the authorization code.'
    #code = raw_input("Enter the authorization code here: ").strip()

    # This will fail if the user enters an invalid authorization code
    #access_token, user_id = flow.finish(code)

    client = dropbox.client.DropboxClient('NVkhEjuWdRAAAAAAAAAADe5DY4rB159Qpi6xyq7ZrFowPNbJcs23noGMNyPu5d5E')
    #print 'linked account: ', client.account_info()
    #respuesta = client.file_delete('/hp.txt')
    archivo = open('output.json', 'rb')
    response = client.put_file('/outputNotas.json', archivo, True)
    #print 'uploaded: ', response