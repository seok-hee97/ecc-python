	
import hashlib
import codecs

privateKey = 11253563012059685825953619222107823549092147699031672238385790369351542642469

publicKey = 36422191471907241029883925342251831624200921388586025344128047678873736520530, 20277110887056303803699431755396003735040374760118964734768299847012543114150

x0 = 55066263022277343669578718895168534326250603453777594175500187360389116729240
y0 = 32670510020758816978083085130507043184471273380659243275938904335757337482424

	
publicKeyHex = "04"+hex(publicKey[0])[2:]+hex(publicKey[1])[2:]


	
def hexStringToByte(content):
    return codecs.decode(content.encode("utf-8"), 'hex')
 
def hashHex(algorithm, content):
    my_sha = hashlib.new(algorithm)
    my_sha.update(hexStringToByte(content))
    return my_sha.hexdigest()

# ------------------------------------------

# hash of public key
output = hashHex('sha256', publicKeyHex)
output = hashHex('ripemd160', output)
output = "00" + output

print("hash of public key : ", output)

# -----------------------------------------------------

checksum = hashHex('sha256', hashHex('sha256', output))
checksum = checksum[0:8]

print("checksum : ?", checksum )

# -------------------------------------
	
address = output+checksum

print("25 byte binary address : ", address)

import base58

address = str(base58.b58encode(hexStringToByte(address)))
print("bitcoing address : ", address[2:len(address)-1])