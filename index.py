/*token checker muy basico, si llegaras a requerir de una herramienta que revise todo sobre una cuenta de discord
    no dudes en contactarme, puedo hacer uno que revise mensajes, servidores, amigos, suscripcion, creacion etc*/
import requests
from colorama import init, Fore, Style

init()  

def get_user_data(token):
    try:
        response = requests.get('https://discordapp.com/api/v9/users/@me', headers={'Authorization': token})
        response.raise_for_status()  # Generar una excepción si la respuesta no es exitosa
        data = response.json()

        print(Fore.RED + 'Token válido.')
        print(Fore.RED + f'Correo: {Fore.YELLOW}{data["email"]}')
        print(Fore.RED + f'Número: {Fore.YELLOW}{data.get("phone", "No disponible")}')
        print(Fore.RED + f'Usuario: {Fore.YELLOW}{data["username"]}#{data["discriminator"]} ({data["id"]})')

        user_data = {
            'token': token.replace('"', ''),
            'correo': data['email'],
            'numero': data.get('phone', 'No disponible'),
            'usuario': f'{data["username"]}#{data["discriminator"]}',
            'revisado': True
        }

        return user_data
    except requests.exceptions.RequestException as error:
        print(Fore.RED + f'Error: {error}')
        return None

def main():
    print(Fore.RED + '''
  ██╗░░██╗██╗░░░██╗██████╗░███████╗████████╗██╗░░██╗██████╗░███████╗░█████╗░██████╗░░██████╗
  ██║░░██║╚██╗░██╔╝██╔══██╗██╔════╝╚══██╔══╝██║░░██║██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝
  ███████║░╚████╔╝░██████╔╝█████╗░░░░░██║░░░███████║██████╔╝█████╗░░███████║██║░░██║╚█████╗░
  ██╔══██║░░╚██╔╝░░██╔═══╝░██╔══╝░░░░░██║░░░██╔══██║██╔══██╗██╔══╝░░██╔══██║██║░░██║░╚═══██╗
  ██║░░██║░░░██║░░░██║░░░░░███████╗░░░██║░░░██║░░██║██║░░██║███████╗██║░░██║██████╔╝██████╔╝
  ╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░╚══════╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═════╝░╚═════╝░
  token checker(script: basico)
  by zelensky#0001
  my server https://discord.gg/hypethreads''')

    token = input(Fore.RED + 'Ingrese el token que desea revisar: ')
    if not token:
        print(Fore.RED + 'Token no válido.')
    else:
        token = token.replace('"', '')
        print('')
        print(Fore.RED + f'Token en revisión: {Fore.YELLOW}{token}')
        print('')

        user_data = get_user_data(token)

        if user_data:
            print('')
            print(Fore.RED + '=== Revisión de Tokens finalizada ===')
            print('')
            print(Fore.RED + 'Usuarios revisados: 1')

if __name__ == '__main__':
    main()
