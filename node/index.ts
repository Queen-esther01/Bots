import { Bot } from 'grammy'

const bot = new Bot(process.env.BOT_TOKEN as string)

bot.command("start", async (ctx) => {

    await ctx.reply("Hello, welcome to the bot!")
})

bot.on("message:text", (ctx: { message: { text: any }; reply: (arg0: string) => void }) => {
    const text = ctx.message.text
    if (text === "hi") {
        ctx.reply("Hello, how are you?")
    }
    else{
        ctx.reply("This is a test bot")
    }
})

bot.start()
