use std::{env, fs::{File,}, io::{BufRead, BufReader}};
fn main() {
    let args:Vec<String>=env::args().collect();
    let file_path :String = args[1].clone();
    let word :String = args[2].clone();

    println!("filepath:{},word:{}",file_path,word);
    let  file =match File::open(file_path){
        Ok(file) => file,
        Err(error)=>{
            println!("Failed to open the file {}",error);
            return;
        }
    };
    //let pattern =word.as_bytes();
    let mut reader = BufReader::with_capacity(8*1024*1024, file);
    let mut count = 0;
    loop {
        let buffer = reader.fill_buf().unwrap();
        if buffer.is_empty(){
            println!("Done");
            break;
        }
        let to_string =String::from_utf8_lossy(buffer);
        
        match to_string.find(&word){
            Some(index)=>{
            count=count+1;
            let start = index-20;
            let end = index+word.len()+20;
            println!("found the word here {}",&to_string[start..end])}
            ,
            None=>{}
        }
        reader.consume(8*1024*1024);
    }

}
