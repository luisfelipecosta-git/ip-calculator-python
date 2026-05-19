import ipaddress

ip = input("Digite um endereço IP com máscara (ex: 192.168.1.1/24): ")

try:
    network = ipaddress.ip_network(ip, strict=False)

    print(f"\nRede: {network.network_address}")
    print(f"Broadcast: {network.broadcast_address}")
    print(f"Máscara: {network.netmask}")
    print(f"Quantidade de hosts: {network.num_addresses - 2}")

except ValueError:
    print("IP inválido.")
