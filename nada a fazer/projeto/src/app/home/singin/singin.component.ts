import { Component, OnInit } from "@angular/core";
import { FormBuilder, FormGroup } from "@angular/forms";

@Component({
    templateUrl: './singnin.component.html'
})
//@ts-ignore
export class SignInComponent implements OnInit {
//@ts-ignore
    loginForm: FormGroup;

    constructor(private formBuilder: FormBuilder) { }
    ngOnInit(): void {
        throw new Error("Method not implemented.");
    }
}