
def get_modules_script(script_name):
    '''
    Args:
        script_name:
    Returns:
        
    '''
    all = []

    for m in settings.MODULE_LIST:
        if hasattr(m, script_name):
            all.append(getattr(m, script_name))
            continue

        try:
            all.append(__import__('%s.%s' % (m.__name__, script_name), 
                globals(), locals(), [m.__name__]))
        except ImportError, e:
            #print repr(type(e)) + m.__name__ + ":" + str(e)
            pass
        except:
            import traceback
            msg = "Error importing %s from module %s: \n %s" % (
                script_name, m, traceback.format_exc()
            )
    return all