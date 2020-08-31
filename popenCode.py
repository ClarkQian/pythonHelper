def exec(cmd:str):
    pip = os.popen(cmd) # 这个地方不能合并一行写，会出错说 read of closed file
    return pip.buffer.read().decode(encoding='utf8')
