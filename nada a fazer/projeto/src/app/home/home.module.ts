import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { SignInComponent } from './singin/singin.component';

@NgModule({
    imports: [
        FormsModule,
       ],
    //@ts-ignore
    declarations: [ SignInComponent ]
})
export class HomeModule { }