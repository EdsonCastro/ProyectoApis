# Include the Dropbox SDK
import dropbox

# Get your app key and secret from the Dropbox developer website
def actulizarNotasDropbox():
    app_key = '887r2dpkbvj5l3e'
    app_secret = 'lqd33odxs1ada3t'

    flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
    client = dropbox.client.DropboxClient('NVkhEjuWdRAAAAAAAAAADe5DY4rB159Qpi6xyq7ZrFowPNbJcs23noGMNyPu5d5E')

    archivo = open('outputNotas.json', 'rb')
    response = client.put_file('/outputNotas.json', archivo, True)
    #print 'uploaded: ', response
    
    
def descargarTabla():
    app_key = '887r2dpkbvj5l3e'
    app_secret = 'lqd33odxs1ada3t'

    flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
    client = dropbox.client.DropboxClient('NVkhEjuWdRAAAAAAAAAADe5DY4rB159Qpi6xyq7ZrFowPNbJcs23noGMNyPu5d5E')
    #folder_metadata = client.metadata('/')
    #print 'metadata: ', folder_metadata
    #f = open('outputNotas.json', 'rb')    
    f, metadata = client.get_file_and_metadata('/outputNotas.json')
    print metadata
    out = open('outputNotas.json', 'wb')
    out.write(f.read())
    out.close()
    
    