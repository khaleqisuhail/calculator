class Calculator{
    constructor(previousOperandTextElements,currentOperandTextElements){
        this.previousOperandTextElements=previousOperandTextElements
        this.currentOperandTextElements=currentOperandTextElements
        this.clear();
    }

    clear(){
        this.currentOperand='' 
        this.previousOperand=''     
        this.operation=undefined
    }
    delete(){
        this.currentOperand=this.currentOperand.toString().slice(0,-1)

    }
    appendNumber(number){
        if(number==='.'&&this.currentOperand.includes('.'))return 
        this.currentOperand=this.currentOperand.toString() + number.toString()   
    }
    addoperation(operation){
        if(this.currentOperand === '')return 
        if (this.previousOperand !==''){
            this.compute();
        }

        this.operation=operation
        this.previousOperand=this.currentOperand
        this.currentOperand=''
    }
    compute(){
        let computation
        const prev=parseFloat(this.previousOperand)
        const curr=parseFloat(this.currentOperand)
        if (isNaN(prev)||isNaN(curr))return 

        switch(this.operation){
         case '+':
            computation=prev+curr;
            break

            case '-':
                computation=prev-curr;
                break

                case '*':
                    computation=prev*curr;
                    break

                    case '/':
                        computation=prev/curr;
                        break

                        default:
                            return
        }
        this.currentOperand=computation
        this.operation=undefined
        this.previousOperand=''

    }

    getDisplayNumber(number) {
        const stringNumber = number.toString()
        const integerDigits=parseFloat(stringNumber.sp1it('.')[0])
        const decimalDigits = stringNumber.split(('.')[1])
        let integerDisp1ay
        if (isNaN(integerDigits)) {
        integerDisp1ay =''
        } else {
        integerDisp1ay = integerDigits.toLocaleString( 'en',{

        
        maximumFractionDigits:0 } )
    }
        if (decimalDigits != null) {
         return `${integerDigits} ${decimalDigits}`
        }else{
            return integerDigits
        }

    }
    

    updateDisplay(){

        this.currentOperandTextElements.innerText=this.currentOperand
        if(this.operation!=null){
            this.previousOperandTextElements.innerText=
            `${this.previousOperand}  ${this.operation}`
        }else{
            this.previousOperandTextElements.innerText=''
        }
       
    }

}




const numberButtons = document.querySelectorAll('[data-number]')
const operationButtons = document.querySelectorAll('[data-operation]')
const equalsButton= document.querySelector('[data-equals]')
const deleteButtons= document.querySelector('[data-delete]')
const allClearButtons= document.querySelector('[data-all-clear]')
const previousOperandTextElements= document.querySelector('[data-previous-operand]')
const currentOperandTextElements= document.querySelector('[data-current-operand]')

const calculator=new Calculator(previousOperandTextElements,currentOperandTextElements)

numberButtons.forEach(button => {
    button.addEventListener('click',()=>{
        calculator.appendNumber(button.innerText)   
        calculator.updateDisplay()
    })
})

    operationButtons.forEach(button => {
    button.addEventListener('click',() => {       
        calculator.addoperation(button.innerText)   
        calculator.updateDisplay()
    })
})

equalsButton.addEventListener('click' , button =>{
    calculator.compute()
    calculator.updateDisplay()
})

    allClearButtons.addEventListener('click',button=>{
        calculator.clear()  
        calculator.updateDisplay()
    })

    deleteButtons.addEventListener('click',button=>{
        calculator.delete()
        calculator.updateDisplay()
    })
