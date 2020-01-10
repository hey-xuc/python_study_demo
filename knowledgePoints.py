@property  私有装饰符  将属性定义为私有不可访问的，
    @property
    def demo():
        return 返回属性的名称
@<attr>.setter  设置私有属性方法装饰符，外部访问私有属性之前会调用此方法，
                一般用来赋值私有属性前检验有效值，与之对应的装饰符有
                @<attr>.getter
    @demo.setattr
    def demo():
        return 检验修改后的值
    
__slots__   限定对象只能拥有哪些属性

@staticmethod   定义静态方法
@classmethod    定义类方法
@abstractmethod     定义抽象方法
__str__     使用print打印对象的时候会自动调用此方法

定义抽象类
from adc import ABCMeta, abstractmtthod
class demo(object, metaclass=ABCMeta)

类之间三种关系
    is-a 继承关系，比如人和学生，手机和电子产品
    has-a 关联关系，部门和员工，关联关系如果是整体和
        部分的关联称之为聚合关系，如果整体进一步负责了
        部分的生命周期称之为合成关系，最强关联关系
    use-a 依赖关系，比如司机有一个驾驶的行为（方法）
        其中参数用到了汽车，那么司机和汽车就称之为
        依赖关系
        
开发GUI应用的5个步骤
    1.导入tkinter模块中我们需要的东西
    2.创建一个顶层窗口对象并用它来承载整个GUI应用
    3.在顶层窗口对象上添加GUI组件
    4.通过代码将这些GUI组件功能组织起来
    5.进入主事件循环
    
    
pygame 开发平面小游戏的库
panda3D 3D游戏库
tkinter Python GUI默认模块库
        

