from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import calc


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def print_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    print(msg)
    items = msg.split()
    num1 = items[1]
    num2 = items[3]
    oper = items[2]
    result = calc.op1(num1,num2,oper)
    await update.message.reply_text(f'{num1} {oper} {num2} = {result}')    

app = ApplicationBuilder().token('5904425625:AAEXeJ8OX5N4QUWEaapYSzQeo0zqxHgMxSc').build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("print", print_command))
print('server start')
app.run_polling()