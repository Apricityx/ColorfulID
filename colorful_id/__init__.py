from mcdreforged.api.command import *
from mcdreforged.api.types import PluginServerInterface, Info
from mcdreforged.command.command_source import PlayerCommandSource

team_name = ['__red', '__blue', '__green', '__yellow', '__light_purple', '__aqua', '__white', '__black', '__gray',
             '__gold', '__dark_red', '__dark_blue', '__dark_green', '__dark_aqua', '__dark_purple', '__dark_gray',
             ]
color = ['red', 'blue', 'green', 'yellow', 'light_purple', 'aqua', 'white', 'black', 'gray', 'gold', 'dark_red',
         'dark_blue', 'dark_green', 'dark_aqua', 'dark_purple', 'dark_gray']


def init_teams(server: 'PluginServerInterface'):
    global team_name
    global color
    for i in range(len(team_name)):
        server.execute('team add ' + team_name[i])
        server.execute('team modify ' + team_name[i] + ' color ' + color[i])


def uninstall(server: 'PluginServerInterface'):
    global team_name
    for i in range(len(team_name)):
        server.execute('team remove ' + team_name[i])


def execute(source: 'PlayerCommandSource', info: Info):  # source：是一个玩家对象，info：是一个消息对象
    # 进行判断，如果是玩家输入的指令，就执行
    get_server = source.get_server()
    if source.is_player:
        arg = source.get_info().content.split(' ')[1]
        if arg == 'install':
            init_teams(get_server)
        elif arg == 'uninstall':
            uninstall(get_server)
        elif arg == 'red':
            get_server.execute('execute as ' + source.player + ' run team join __red ' + source.player)
            get_server.execute('tell @a ' + '已将' + source.player + '染色')
        elif arg == 'blue':
            get_server.execute('execute as ' + source.player + ' run team join __blue ' + source.player)
            get_server.execute('tell @a ' + '已将' + source.player + '染色')
        elif arg == 'green':
            get_server.execute('execute as ' + source.player + ' run team join __green ' + source.player)
            get_server.execute('tell @a ' + '已将' + source.player + '染色')
        elif arg == 'yellow':
            get_server.execute('execute as ' + source.player + ' run team join __yellow ' + source.player)
            get_server.execute('tell @a ' + '已将' + source.player + '染色')
        elif arg == 'light_purple':
            get_server.execute('execute as ' + source.player + ' run team join __light_purple ' + source.player)
            get_server.execute('tell @a ' + '已将' + source.player + '染色')
        elif arg == 'aqua':
            get_server.execute('execute as ' + source.player + ' run team join __aqua ' + source.player)
            get_server.execute('tell @a ' + '已将' + source.player + '染色')
        elif arg == 'white':
            get_server.execute('execute as ' + source.player + ' run team join __white ' + source.player)
            get_server.execute('tell @a ' + '已将' + source.player + '染色')
        elif arg == 'black':
            get_server.execute('execute as ' + source.player + ' run team join __black ' + source.player)
            get_server.execute('tell @a ' + '已将' + source.player + '染色')
        elif arg == 'gray':
            get_server.execute('execute as ' + source.player + ' run team join __gray ' + source.player)
            get_server.execute('tell @a ' + '已将' + source.player + '染色')
        elif arg == 'gold':
            get_server.execute('execute as ' + source.player + ' run team join __gold ' + source.player)
            get_server.execute('tell @a ' + '已将' + source.player + '染色')
        elif arg == 'dark_red':
            get_server.execute('execute as ' + source.player + ' run team join __dark_red ' + source.player)
            get_server.execute('tell @a ' + '已将' + source.player + '染色')
        elif arg == 'dark_blue':
            get_server.execute('execute as ' + source.player + ' run team join __dark_blue ' + source.player)
            get_server.execute('tell @a ' + '已将' + source.player + '染色')
        elif arg == 'dark_green':
            get_server.execute('execute as ' + source.player + ' run team join __dark_green ' + source.player)
            get_server.execute('tell @a ' + '已将' + source.player + '染色')
        elif arg == 'dark_aqua':
            get_server.execute('execute as ' + source.player + ' run team join __dark_aqua ' + source.player)
            get_server.execute('tell @a ' + '已将' + source.player + '染色')
        elif arg == 'dark_purple':
            get_server.execute('execute as ' + source.player + ' run team join __dark_purple ' + source.player)
            get_server.execute('tell @a ' + '已将' + source.player + '染色')
        elif arg == 'dark_gray':
            get_server.execute('execute as ' + source.player + ' run team join __dark_gray ' + source.player)
            get_server.execute('tell @a ' + '已将' + source.player + '染色')
        else:
            get_server.execute(
                'tellraw ' + source.player + ' "可用颜色：red,blue,green,yellow,purple,aqua,white,black,gray,gold,dark_red,dark_blue,dark_green,dark_aqua,dark_purple,dark_gray,dark_gold" ')
    else:
        get_server.logger.info('!!color 只能由玩家执行')


def on_load(server: 'PluginServerInterface', old):
    server.register_command(
        Literal('!!color').then(
            Text('arg').
            runs(execute)
        )
    )
