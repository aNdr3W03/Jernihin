const getYear = new Date().getFullYear();

const isNumber = event => {
    var charCode = (event.which) ? event.which : event.keyCode;
    if (charCode > 31 && (charCode != 46 &&(charCode < 48 || charCode > 57)))
        return false;
    return true;
}
