from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config = {
    'secure_connect_bundle': 'C:\\Users\\Nitiraj\\Dropbox\\PC\\Desktop\\Summer\\Summer\\src\\resources\\secure-connect-nitiraj-singh-chouhan .zip'
}

auth_provider = PlainTextAuthProvider('FBmZKgnOLNCKdZsxrupyDxvT', 'Qd2bed6nzj,_pCewHcD_WSQ7pfpx6x.RtboNBzgPmuoTh6BDZh5r9G9m2Qfrq-Pb+LaPMSB2uTMljEig7uabHqZ2XoeozE19uEMLmLkIN+dKJofroUPP7hcbPGMi+8Ln')

cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

row = session.execute("select release_version from system.local").one()
if row:
    print(row[0])
else:
    print("An error occurred.")
