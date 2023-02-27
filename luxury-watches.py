# Create a class representing a luxury watch.
# The class should allow you to hold a number of watches created in the
# watches_created class variable. The number could be fetched using a
# class method named get_number_of_watches_created;
# the class may allow you to create a watch with a dedicated engraving
# (text). As this is an extra option, the watch with the engraving
# should be created using an alternative constructor (a class method),
# as a regular __init__ method should not allow ordering engravings;
# the regular __init__ method should only increase the value of the
# appropriate class variable;

# The text intended to be engraved should follow some restrictions:
#
# it should not be longer than 40 characters;
# it should consist of alphanumerical characters, so no space characters
# are allowed;
# if the text does not comply with restrictions, an exception should be raised;
# before engraving the desired text, the text should be validated against
# restrictions using a dedicated static method.
#
# Create a watch with no engraving
# Create a watch with correct text for engraving
# Try to create a watch with incorrect text, like 'foo@baz.com'. Handle
# the exception
# After each watch is created, call class method to see if the counter
# variable was increased

class NoEngraving(Exception):
    pass


class LuxuryWatch:
    _watches = 0
    _watches_with_engraving = 0

    def __init__(self):
        LuxuryWatch._watches += 1

    @classmethod
    def watch_with_engraving(cls, text):
        if LuxuryWatch.restrictions:
            _engraved_watch = cls()
            _engraved_watch.text = text
            LuxuryWatch._watches_with_engraving += 1
            return _engraved_watch
        else:
            return "Watch can not be engraved."

    @staticmethod
    def restrictions(text):
        try:
            if len(text) < 41 and text.isalnum:
                return
            else:
                raise NoEngraving
        except NoEngraving:
            print("Text should not be longer than 40 characters;"
                  "it should consist only of alphanumerical characters.")

    @classmethod
    def get_num_watch(cls):
        print("Watches created: \t{1}, with engraving {0}".format\
                (LuxuryWatch._watches_with_engraving, LuxuryWatch._watches))


watch1 = LuxuryWatch()
watch1.get_num_watch()
watch2 = LuxuryWatch.watch_with_engraving("Roxana")
watch1.get_num_watch()
watch3 = LuxuryWatch.watch_with_engraving("@hey you")
watch1.get_num_watch()
