import {writable} from 'svelte/store'
import {tweened} from 'svelte/motion'
import {cubicOut} from 'svelte/easing'

import expenseService from './ExpenseService.js'
 
let expensesFirestore = []; 
const store = writable([]);


let items = await expenseService.read()

items.forEach(doc =>{
	expensesFirestore = [
	...expensesFirestore,
	{
		id:doc.id,
		date:doc.date,
		paymentType:doc.paymentType,
		category:doc.category,
		amount:doc.amount,
		quantity:doc.quantity,
		subtotal:doc.subtotal
	}]
})

store.set(expensesFirestore)


export const totalTweenStore = tweened(0,{
	duration:600,
	delay: 800,
	easing: cubicOut
})
export default store;