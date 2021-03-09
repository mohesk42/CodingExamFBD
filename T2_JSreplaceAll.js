function replaceAll(txt, old, newT){
    if(old != newT && old !=""){
        while(txt.indexOf(old)!=-1){
            txt = txt.replace(old, newT);
        }
        return txt;
    }
    else{
        return txt;
    } 
}
