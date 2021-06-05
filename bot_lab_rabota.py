import pandas
import telebot



class labbot:
    help_text = '''
/categories - выдать названия всех категорий, которые вы спарсили. 
/categories {Название категории} - выдать товары этой категории.
/product {название продукта} - выдать информацию о данном товаре
'''
    categories = pandas.read_csv('electronic.csv')

    def show(self, args):
        if len(args) <= 0:
            return '\n'.join(self.categories)
        else:
            if args == "categories":
                frac = (f' названия всех категорий "{args}"')
            else:
                frac = (f'выдать товары этой категории "{args}"')

        if (frac) not in self.categories:
            return f'Товара с названием: {args} не существует'
        else:
            dep = self.categories[self.categories.categories == frac]
            dep = dep[1:11].to_string()
        return dep

TOKEN = '1757180094:AAHgzPC5sabv7N30Lc7H3U9G8mRkVwF6_xU'

bot = telebot.TeleBot(TOKEN)
kbot = labbot()


@bot.message_handler(commands=['start', 'help'])
def show(message):
    bot.send_message(message.chat.id, kbot.help_text)


@bot.message_handler(commands=['categories'])
def categories(message):
    args = message.text[11:]
    bot.send_message(message.chat.id, kbot.show(args))


if __name__ == '__main__':
    bot.polling()