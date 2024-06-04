import discord
from controllers import code_input_controller, code_redeemer_controller, notification_controller

def main():
    client = discord.Client()

    @client.event
    async def on_ready():
        print('Logged on as {0}!'.format(client.user))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('!redeem'):
            promo_code = message.content.split(' ')[1]
            success, error_message = code_redeemer_controller.redeem_code(promo_code)
            if success:
                await message.channel.send(f'Promo code {promo_code} redeemed successfully!')
            else:
                await message.channel.send(f'Failed to redeem promo code {promo_code}. Error: {error_message}')

    client.run('your_token_here')

if __name__ == '__main__':
    main()