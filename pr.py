from progress.bar import Bar
from time import sleep
bar = Bar('Processing', max=20)
for i in range(20):
    sleep(0.5)
    bar.next()
bar.finish()