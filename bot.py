import discord
from discord.ext import commands
import asyncio
import os
import datetime

client = discord.Client()
@client.event
async def on_ready():
    print('logged in')

engdap = {"조랭봇 부활절 달걀":"곧 부활절이네요. 아니면 이미 지났을 수도 있지만,\n이 메시지를 발견하신 분에게 약간의 이스터에그 힌트를 드릴게요.\n**영타**","조랭봇 안녕":"안녕하세요!","조랭봇 안녕하세요":"안녕하세요!","조랭봇 하이":"안녕하세요!","조랭봇 잘가":"안녕히 가세요 :wave:","조랭봇 조랭":"||내가 존재하는 이유||","조랭봇 뭐해":"저는 사실 기계 안에서 노동을 하고 ㅇ... 살려주세요!!!","조랭봇 사랑해":"에?","조랭봇 사귀자":"에?","조랭봇 꺼져":"싫어요 켜져있을거예요","조랭봇 랭조":"||어쩔티비||","조랭봇 mrpdjxmtld":"축하합니다! 당신은 이스터에그를 발견하셨습니다!\n고로 당신은 크리님의 서버에 들어올 수 있을 예정이였으나 홍보 금지로 제작자한테 철퇴맞음","조랭봇 크리멍청이":"아 님 멍청이라고요?","조랭봇 ㅎㅇ":"안녕하세요.","조랭봇 ㅂㅇ":"안녕히계세요.","조랭봇 이스터에그":"그걸 알려줄것 같냐? ㅋㅋㅋ.","조랭봇 조랭봇":"저는 발달된 인공지능은 아니고 그냥 커맨드형식으로 만들어진 봇입니다","조랭봇 자기소개":"저는 크리님에 의해 만들어진 응답 봇이랍니다.","조랭봇 크리":"저를 만드신 분이예요!"}

#조랭봇 멤버 개발하기
#for member in message.guilds.members: 써서

@client.event
async def on_message(message):
    if message.content.startswith('조랭봇 '):
        if message.content == "조랭봇":
            await message.channel.send("부르셨나요?")
        elif message.content == "조랭봇 도움말" or message.content == "조랭봇 명령어" or message.content == "조랭봇 커맨드":
            now = "-----------------------------------\n"
            for key,value in engdap.items():
                if not key == "조랭봇 mrpdjxmtld":
                    now = now + (key+": "+value+"\n-----------------------------------\n")
            await message.channel.send(now)
        elif message.content == "조랭봇 내정보":
            user = message.author
            date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
            await message.channel.send(f"{message.author.mention}\n가입일: {date.year}/{date.month}/{date.day}\n닉네임: {user.name}\n서버 닉네임: {user.display_name}\n아이디: {user.id}")
            await message.channel.send(message.author.avatar_url)
            await message.channel.send("소스 출처: 제이크#2214")
        else:
            try:
                await message.channel.send(engdap[message.content])
            except:
                await message.channel.send("아직 모르는 단어예요! \n조랭봇에게 단어를 가르치고 싶으시다면 kri#1896에게 문의해 주세요!")

client.run(os.environ['token'])