//用多线程复刻上单刺杀叔叔珍贵录像

public class Chatting_Demo1 {

    public static void main(String[] args) {
        //要实现一个简单聊天的功能

        Sender sender = new Sender();
        Reciever reciever = new Reciever();

        sender.start();
        reciever.start();
        //运行程序

    }
}

  class Sender extends Thread {
//叔叔方
      @Override
      public void run() {

          Chatter shushu = new Chatter();
          shushu.name = "陈睿";
          shushu.content = "你所热爱的，就是你的生活。";

          shushu.send();

          }
      }

    class Reciever extends Thread {

    @Override
    public void run() {
    //上单方
        Chatter shangdan = new Chatter();
        shangdan.name = "蒙古上单";
        shangdan.content = "陈睿，你吗什么时候死啊";

        shangdan.reply();

        }
    }

    class Chatter {
        boolean condition = true;

        String name;
        String content;

        //叔叔首先发送信息
        public synchronized void send() {
            if (condition = false) {
                try {
                    this.wait(500);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }

            System.out.println(this.name + ":" + this.content);
            //输出内容

            this.notifyAll();//通知另外一个人回复
            this.condition = false;
        }

        //上单接收后回复消息
        public synchronized void reply() {
            if (condition = true) {
                try {
                    this.wait(500);//等待叔叔发送消息过来
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }

            System.out.println(this.name + ":" + this.content);
            //输出内容

            this.notifyAll();//通知叔叔
            this.condition = true;
        }
    }
