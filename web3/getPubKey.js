const ethers = require("ethers")

const ad = "0xd22213f7B4E5997C9B542105cce6ed4dfEAE5F91"

getPubKey = async () => {
 const infuraProvider = new ethers.providers.JsonRpcProvider(
  "https://ropsten.infura.io/v3/0c81b9e9bfa9442eae485ac59c3e3816"
 )
 const tx = await infuraProvider.getTransaction(
  "0x6174abcf8b440f346acec02aad847f4082663bcbbed86af78bbf62f9a3ace192"
 )
 const expandedSig = {
  r: tx.r,
  s: tx.s,
  v: tx.v
 }
 const signature = ethers.utils.joinSignature(expandedSig)
 const txData = {
  gasPrice: tx.gasPrice,
  gasLimit: tx.gasLimit,
  value: tx.value,
  nonce: tx.nonce,
  data: tx.data,
  chainId: tx.chainId,
  to: tx.to
 }
 const rsTx = await ethers.utils.resolveProperties(txData)
 const raw = ethers.utils.serializeTransaction(rsTx) // returns RLP encoded tx
 const msgHash = ethers.utils.keccak256(raw) // as specified by ECDSA
 const msgBytes = ethers.utils.arrayify(msgHash) // create binary hash
 const recoveredPubKey = ethers.utils.recoverPublicKey(msgBytes, signature)
 const recoveredAddress = ethers.utils.recoverAddress(msgBytes, signature)
 console.log(recoveredAddress)
 console.log(recoveredPubKey)
 console.log("Correct address:", recoveredAddress === ad)
}

getPubKey()
