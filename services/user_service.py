from models.user import User
from sqlalchemy.orm import Session
from auth.hash import hash_password, verify_password

def create_user(db: Session, user_data):
    hashed = hash_password(user_data.password)
    
    new_user = User(
        name=user_data.name,
        email=user_data.email,
        password=hashed
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user


def authenticate_user(db: Session, email, password):
    user = db.query(User).filter(User.email == email).first()
    
    if not user:
        return None
    
    if not verify_password(password, user.password):
        return None
    
    return user