ans1 = '*123*1a2b3c4d5c6d7a8d9b10a11d12c13d14c15a16a17d18b19b20a21c22d23b24d25a26d27b28c29a30c'
client1 = '*12*1a2b3a4d5d6d7c8d9b10a11d12c13d14c15a16a17d18b19b20a21c22d23b24d25a26d27b28c29a30c'
key_admin = []
key_client = []


data_base = {}

key_admin.append(ans1[1:ans1.rfind('*')])
key_client.append(client1[1:client1.rfind('*')])
answer_admin = ans1[ans1.rfind('*') + 1:]
answer_client = client1[client1.rfind('*') + 1:]

def func():



print(key_admin)
print(key_client)
print(answer_admin)
print(answer_client)



