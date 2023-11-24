db = db.getSiblingDB('test_db')
db.templates.remove({});
db.createCollection('questions');
db.questions.insert(
        {
      "id": 1,
      "parent_id": 0,
      "text": "Что делать Диме дальше?",
      "level_id": 1
    });

db.questions.insert(
        {
      "id": 2,
      "parent_id": 1,
      "text": "Что делать Диме дальше?",
      "level_id": 2
    });

db.createCollection('answers');
db.answers.insert(
      {
      "id": 1,
      "level_id": 1,
      "question_id": 1,
      "parent_id": 0,
      "text": "Ввести данные карты, так как цена довольно привлекательная",
      "message": "Вы были обмануты",
      "video_id": 2,
      "correct": false
    });

db.answers.insert({
      "id": 2,
      "level_id": 1,
      "question_id": 1,
      "video_id": 3,
      "text": "Засомневаться в том, что на этом сайте можно что-то покупать, посоветоваться с взрослыми",
      "message": null,
      "correct": true
    });
db.answers.insert({
      "id": 3,
      "level_id": 1,
      "question_id": 1,
      "video_id": 4,
      "text": "Передумать покупать",
      "message": "Верно, если ты не уверен в том, что скидываешь деньги не мошенникам, то лучше на время отложить покупку и узнать получше все детали покупки инвентаря для игры у одноклассника.",
      "correct": true
    });
db.answers.insert({
      "id": 4,
      "level_id": 2,
      "question_id": 2,
      "video_id": 5,
      "text": "Купить инвентарь на этом сайте на зло папе",
      "message": null,
      "correct": false
    });
db.answers.insert();
db.answers.insert();