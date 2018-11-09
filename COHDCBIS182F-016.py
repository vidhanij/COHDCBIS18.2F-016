plaintext = input('THEDIEHASBEENCAST : ')
alphabet = "abcdefghijklmnopqrstuvwxyz"
k = 3
cipher =''

for c in plaintext:
    if c in alphabet:
        cipher += alphabet[(alphabet.index(c)+k)% (len(alphabet))]
        
        print('Encrypted Message : '+ cipher)
    
