# �C���X�g�[������ discord.py ��ǂݍ���
import discord
import random

# ������Bot�̃A�N�Z�X�g�[�N���ɒu�������Ă�������
TOKEN = 'NTA0Njg4ODA5ODQ2NTA1NDcz.XYzHgQ.2pqbM7tfQnUk9Ydzg-cunbx03LY'

# �ڑ��ɕK�v�ȃI�u�W�F�N�g�𐶐�
client = discord.Client()



# �N�����ɓ��삷�鏈��
@client.event
async def on_ready():
    # �N��������^�[�~�i���Ƀ��O�C���ʒm���\�������
    print('���O�C�����܂���')

# ���b�Z�[�W��M���ɓ��삷�鏈��
@client.event
async def on_message(message):
    # ���b�Z�[�W���M�҂�Bot�������ꍇ�͖�������
    if message.author.bot:
        return
    # �u/neko�v�Ɣ���������u�ɂ�[��v���Ԃ鏈��
    if message.content == '�I�Ȃ�':
	random.uniform(0,3)
	if random.uniform == 0
        await message.channel.send('�E�z�E�z')
if random.uniform == 1
        await message.channel.send('���͂Ȃ����I�I�I�I�I�I')
if random.uniform == 2
        await message.channel.send('�Ӂ[��')
if random.uniform == 3
        await message.channel.send('���؂�ꂽ�I�I�I�I�I�I�I')

# Bot�̋N����Discord�T�[�o�[�ւ̐ڑ�
client.run(TOKEN)