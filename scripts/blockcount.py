rom bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
rpc_connection = AuthServiceProxy("http://rpcuser:rpcpass@127.0.0.1:9245", timeout=120)
print(rpc_connection.getblockcount())
