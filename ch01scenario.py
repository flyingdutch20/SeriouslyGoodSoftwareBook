import unittest

# Container a = new Container();
# Container b = new Container();
# Container c = new Container();
# Container d = new Container();

# a.addWater(12);
# d.addWater(8);
# a.connectTo(b);
# System.out.println(a.getAmount()+" "+b.getAmount()+" "+
# c.getAmount()+" "+d.getAmount());

# 6.0 6.0 0.0 8.0

# b.connectTo(c);
# System.out.println(a.getAmount()+" "+b.getAmount()+" "+
# c.getAmount()+" "+d.getAmount());

# 4.0 4.0 4.0 8.0

# b.connectTo(d);
# System.out.println(a.getAmount()+" "+b.getAmount()+" "+
# c.getAmount()+" "+d.getAmount());

# 5.0 5.0 5.0 5.0


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
