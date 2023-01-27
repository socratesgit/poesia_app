db.createUser({
    user: 'user_poesia_errante',
    pwd: 'giuseppe_ungaretti',
    roles: [
        {
            role: 'readWrite',
            db: 'poesia_errante_db'
        }
    ]
})