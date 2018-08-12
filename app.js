const app = require('express')()

app.get('/', (req, res) => {
    res.send('hi')
})

app.listen(3003, _ => console.log(`Up and listening on 3003!!!`))