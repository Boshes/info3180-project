from . import db

class User(db.Model):
    __tablename__ = 'profiles'
    id=db.Column(db.Integer,primary_key=True,nullable=False,unique=True)
    userimage=db.Column(db.String(256))
    username=db.Column(db.String(256),unique=True)
    userfname=db.Column(db.String(256))
    userlname=db.Column(db.String(256))
    userage=db.Column(db.String(120))
    usersex=db.Column(db.String(120))
    userhighscore=db.Column(db.Integer)
    usertdollars=db.Column(db.Integer)
    useraddon=db.Column(db.DateTime,nullable=False)
    
    def __init__(self,userimage,username,userfname,userlname,userage,usersex,useraddon):
        self.userimage = userimage
        self.username = username
        self.userfname = userfname
        self.userlname = userlname
        self.userage = userage
        self.usersex = usersex
        self.userhighscore = 0
        self.usertdollars = 0
        self.useraddon=useraddon
        
        
    def __repr__(self):
        return '<id {}>'.format(self.id)
