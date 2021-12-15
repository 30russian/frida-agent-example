export const app = {
    hookClassMethod: (clazz: string, method: string): void => {
        // send(`Class = ${clazz}; Method = ${method}`);
        Java.perform(() => {
            send(`Class = ${clazz}; Method = ${method}`);
        });
    }
}