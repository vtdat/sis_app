import getmark
import calmark

getmark.getmark()
result = calmark.calmark()
print "Your CPA = " + str(result)
if result >= 3.5:
    print "Xuat sac!"
elif result >= 3.2:
    print "Gioi!"
elif result >= 2.5:
    print "Kha!"
else:
    print "Yeu!"