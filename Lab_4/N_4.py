import time


def path(path):

    def make_decorator(func):
        
        file = open(path, 'w')

        def wrapped(*args, **kwargs):
            
            time0 = time()
            res_func = func(*args, **kwargs)
            time1 = time()

            file.write('1.'+str(time0)+'\n')
            file.write('2.'+' '.join([str(arg) for arg in args])+'\n')
            file.write('3.'+res_func+'\n')
            file.write('4.'+str(time1)+'\n')
            file.write('5.'+str(time0 - time1))
            
            return res_func

        return wrapped

    return make_decorator

