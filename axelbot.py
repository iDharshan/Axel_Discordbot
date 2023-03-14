import discord
from discord.ext import commands
import asyncio

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def token(ctx):
  await ctx.send("Token or lexical unit is the smallest individual unit in a program")

@client.command()
async def keyword(ctx):
  await ctx.send("A keyword is a word having special meaning reserved by programming language.")

@client.command()
async def identifiers(ctx):
  await ctx.send("identifiers are the names given to different parts of the program viz... variables,objects,classes,functions,lists,dictionaries and so forth")

@client.command()
async def operators(ctx):
  await ctx.send("Operators are tokens that trigger some computation/action when applied to varibles and other objects in an expression")

@client.command()
async def operatortype(ctx):
  await ctx.send("Arithmetic operators(+,-,*,/,%,**,//),Bitwise operators(&,^,|),Shift operators(<<,>>),identity operators(is,is not), Relational operators(>,<,>=,<=,==,!=), logical operators(and,or), Assignment operators(=), Membership operators(in,not in), and Arithmetic-assignment operators (/=,+=,-=,*/,%=,**=,//=)"

@client.command()
async def listtype(ctx):
  await ctx.send("A List in python represents a group of comma-separated values of any datatype between square brackets.")

@client.command()
async def tuples(ctx):
  await ctx.send("Tupes represented as group of comma_separated values of any data type within parentheses.")

@client.command()
async def dictionary(ctx):
  await ctx.send("The dictionary is an unordered set of comma-separated key : value pairs, within {}")

@client.command()
async def immutable(ctx):
  await ctx.send("The immutable types are those that can never change thei value in place.")

@client.command()
async def mutable(ctx):
  await ctx.send("The mutable types are those whose values can be changed in place.")

@client.command()
async def expression(ctx):
  await ctx.send("An expression in python is any valid combination of operators and atoms. An expression is composed of one or more operations.")

@client.command()
async def typecasting(ctx):
  await ctx.send("The explicit conversion of an operand to a specific type is called type casting.")

@client.command()
async def ifstatement(ctx):
  await ctx.send("An if statement tests a particular condition,if the condition evalutes to true,a course-of-action is followed.if it fails it returns false and does nothing")

@client.command()
async def nestedif(ctx):
  await ctx.send("A nested if is an if that has another if in its if's body or in elif's body or in its else's body")

@client.command()
async def forloop(ctx):
  await ctx.send("The for loop in python is designed to process the items of any sequence,such as a list or a string,one by one")

@client.command()
async def whileloop(ctx):
  await ctx.send("A while loop is conditional loop that will repeat the instructions within itself as long as a conditional remains true.")

@client.command()
async def breakstatement(ctx):
  await ctx.send("A break statement terminates the very loop it lies within.")

@client.command()
async def continuestatements(ctx):
  await ctx.send("The continue statement forces the next iteration of the loop to take place, skipping any code in between.")


@client.command()
async def hello(ctx):
    await ctx.send("Hey Man!,What up")


@client.command()
async def python(ctx):
    await ctx.send(
        "Python is an interpreted, high-level and general-purpose programming language."
    )


@client.command()
async def hello(ctx):
    await ctx.send("Hey Man!,What up")

@client.command()
async def python(ctx):
    await ctx.send("Python is an interpreted, high-level and general-purpose programming language.")


client.run("ODAxNDQ5MTk1MjQzNzAwMjU1.YAg1ug.JlCuzdVzg2k3qJcl4ltCMXK7CIU")

