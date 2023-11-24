db = db.getSiblingDB('test_db')
db.questions.remove({});
db.answers.remove({});

db.createCollection('questions');
db.questions.insert(
        {
      "id": 1,
      "parent_answer_id": 0,
      "text": "Что делать Диме дальше? (1)",
    });

db.questions.insert(
        {
      "id": 2,
      "parent_answer_id": 2,
      "text": "Что делать Диме дальше? (2)",
    });

db.createCollection('answers');
db.answers.insertMany([
      {
      "id": 1,
      "question_id": 1,
      "parent_id": 0,
      "text": "Ввести данные карты, так как цена довольно привлекательная",
      "message": "Вы были обмануты",
      "video_id": 2,
      "correct": false
    },
    {
      "id": 2,
      "question_id": 1,
      "video_id": 3,
      "text": "Засомневаться в том, что на этом сайте можно что-то покупать, посоветоваться с взрослыми",
      "message": null,
      "correct": true
    },
    {
      "id": 3,
      "question_id": 1,
      "video_id": 4,
      "text": "Передумать покупать",
      "message": "Верно, если ты не уверен в том, что скидываешь деньги не мошенникам, то лучше на время отложить покупку и узнать получше все детали покупки инвентаря для игры у одноклассника.",
      "correct": true
    },
    {
      "id": 4,
      "question_id": 2,
      "video_id": 5,
      "text": "Купить инвентарь на этом сайте на зло папе",
      "message": null,
      "correct": false
    },
    {
      "id": 5,
      "question_id": 2,
      "video_id": 6,
      "text": "Посмотреть отзывы покупателей",
      "message": "Верно, если ты не уверен в том, что скидываешь деньги не мошенникам, то лучше на время отложить покупку и узнать получше все детали покупки инвентаря для игры у одноклассника.",
      "correct": true
    }]);