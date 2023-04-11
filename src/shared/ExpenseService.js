
async function create (expenses) {
	const res = await fetch('http://localhost:9998/lapost', {
		method: 'POST',
		body: JSON.stringify({expenses})
	})
	let data = await res.json()
	return data
}

async function read () {
	const res = await fetch('http://localhost:9998/lapost', {
		method: 'GET',
	})
	let data = await res.json()
	return data
}

async function update (expenses) {
	console.log("update method enter")
	const res = await fetch('http://localhost:9998/edit_piaf', {
		method: 'POST',
		body: JSON.stringify({expenses})
	})
	let data = await res.json()
	return data
}

function delet(argument) {
	// body...
}

const expenseService = {
	create,
	read,
	update,
	delet
}

export default expenseService;